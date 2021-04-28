%rebase('base.tpl', title='News recommendations', path='recommendations')
<html>
<div class="ui label blue">
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