<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.js"></script>
</head>
<body>
<div class="ui container ma-5">
    <h1 class="ui center aligned header">Hacker News Personalizator</h1>
    <div>
        <div class="ui tabular menu">
            <%
                nav_items = [
                    { 'path': 'news', 'title': 'News' },
                    { 'path': 'news_with_labels', 'title': 'Labeled' },
                    { 'path': 'recommendations', 'title': 'Recommendations' },
                ]
            %>
            % for nav_item in nav_items:
                % if path == nav_item['path']:
                <a href="/{{ nav_item['path'] }}" class="active item" class="item">{{ nav_item['title'] }}</a>
                % else:
                <a href="/{{ nav_item['path'] }}" class="item" class="item">{{ nav_item['title'] }}</a>
                % end
            %end
        </div>
    </div>
    <div class="ui container">
        <h1 class="ui header">
        {{ title or 'No title' }}
        </h1>
        <div>
        {{ !base }}
        </div>
    </div>
</div>
</body>
</html>
<style>
    body > .ui.container {
        margin-top: 3rem;
        margin-bottom: 1rem;
    }

    .ui.container {
        padding: 1rem 0;
    }
</style>