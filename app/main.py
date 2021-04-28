from bottle import route, template, redirect, request
from app.db import session, News
from app.helpers import prepare_classifier_data
from app.news_parser import get_news
from app.naive_bayes_classifier import NaiveBayesClassifier
import config


@route('/')
def main():
    redirect('/news')


@route('/news')
def news_list():
    next_id = request.query.next_id or 0
    db_session = session()
    rows = db_session.query(News).filter_by(label=None).all()
    return template('news', rows=rows, next_id=next_id)


@route('/news_with_labels')
def news_list_labels():
    db_session = session()
    rows = db_session.query(News).filter(News.label != None).all()
    return template('news_labeled', rows=rows, next_id=0)


@route('/update_news')
def news_list():
    try:
        next_id = int(request.query.next_id)
    except ValueError:
        return template('error', text='next_id need to be a number')
    db_session = session()
    news = get_news(config.news_url, next_id=next_id)
    next_id = news[-1]['id']
    added = 0
    for news_item_data in news:
        found = db_session.query(News).filter_by(title=news_item_data['title'], author=news_item_data['author']).first()
        if not found:
            news_item = News(
                title=news_item_data['title'],
                author=news_item_data['author'],
                points=news_item_data['points'],
                comments=news_item_data['comments'],
                url=news_item_data['url'],
            )
            db_session.add(news_item)
            added += 1
    db_session.commit()
    print(f'Added {added} news')
    redirect(f'/news?next_id={next_id}')


@route('/add_label')
def add_label():
    label = request.query.label
    news_item_id = request.query.id
    if not label or not news_item_id:
        return template('error', text='label and news_item_id are required parameters')
    db_session = session()
    news_item = db_session.query(News).get(news_item_id)
    news_item.label = label
    db_session.commit()
    redirect_path = request.query.redirect or '/news'
    redirect(redirect_path)


@route('/recommendations')
def recommendations():
    model = NaiveBayesClassifier(alpha=0.05)
    db_session = session()
    train_news = db_session.query(News).filter(News.label != None).all()
    print(f'Train news len: {len(train_news)}')
    X_train, y_train = prepare_classifier_data(train_news)

    news = db_session.query(News).filter_by(label=None).all()
    print(f'Prepare news len: {len(news)}')
    X, _ = prepare_classifier_data(news)
    model.fit(X_train, y_train)
    y = model.predict(X)
    for i in range(len(news)):
        news[i].label = y[i]

    classified_news = [it for it in news if it.label in config.recommendation_labels]
    classified_news = sorted(classified_news, key=lambda x: config.labels_priority.index(x.label))

    return template('news_recommendations', rows=classified_news)
