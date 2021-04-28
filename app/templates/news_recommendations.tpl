<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.js"></script>
</head>
<body>
<div class="ui container" style="padding-top: 10px;">
    <h1 class="ui header">
        News recommendations
    </h1>
    <div>
        Total: {{ len(rows) }}
    </div>
    <table class="ui celled table">
        <thead>
        <th>Title</th>
        <th>Author</th>
        <th>#Likes</th>
        <th>#Comments</th>
        <th>Label</th>
        </thead>
        <tbody>
        %for row in rows:
        <tr>
            <td><a href="{{ row.url }}">{{ row.title }}</a></td>
            <td>{{ row.author }}</td>
            <td>{{ row.points }}</td>
            <td>{{ row.comments }}</td>

            %if row.label == 'good':
            <td class="positive">
                <a class="ui blue ribbon label">Интересно</a>
            </td>
            %elif row.label == 'maybe':
            <td class="active">
                <a class="ui blue ribbon label">Возможно</a>
            </td>
            %end
        </tr>
        %end
        </tbody>
    </table>
</div>
</body>
</html>