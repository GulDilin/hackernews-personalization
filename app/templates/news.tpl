<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.js"></script>
    </head>
    <body>
        <div class="ui container" style="padding-top: 10px;">
          <div>
            Total: {{ len(rows) }}
          </div>
          <table class="ui celled table">
            <thead>
                <th>Title</th>
                <th>Author</th>
                <th>#Likes</th>
                <th>#Comments</th>
                <th colspan="3">Label</th>
            </thead>
            <tbody>
                %for row in rows:
                <tr>
                    <td><a href="{{ row.url }}">{{ row.title }}</a></td>
                    <td>{{ row.author }}</td>
                    <td>{{ row.points }}</td>
                    <td>{{ row.comments }}</td>

                    <td class="positive">
                      %if row.label == 'good':
                      <a class="ui blue ribbon label">Chosen</a>
                      %end
                      <a href="/add_label?label=good&id={{ row.id }}">Интересно</a>
                    </td>
                    <td class="active">
                      %if row.label == 'maybe':
                      <a class="ui blue ribbon label">Chosen</a>
                      %end
                      <a href="/add_label?label=maybe&id={{ row.id }}">Возможно</a>
                    </td>
                    <td class="negative">
                      %if row.label == 'never':
                      <a class="ui blue ribbon label">Chosen</a>
                      %end
                      <a href="/add_label?label=never&id={{ row.id }}">Не интересно</a>
                    </td>
                </tr>
                %end
            </tbody>
            <tfoot class="full-width">
                <tr>
                    <td>
                      <a href="/news_with_labels" class="ui right floated small primary button">Already with labels</a>
                    </td>
                    <td colspan="6">
                        <a href="/update_news?next_id={{ next_id }}" class="ui right floated small primary button">I Wanna more Hacker News!</a>
                    </td>
                </tr>
            </tfoot>
        </table>
        </div>
    </body>
</html>