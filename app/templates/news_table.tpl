<div class="ui label blue">
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
    % setdefault('redirect', 'news')
    % for row in rows:
    <tr>
        <td><a href="{{ row.url }}">{{ row.title }}</a></td>
        <td>{{ row.author }}</td>
        <td>{{ row.points }}</td>
        <td>{{ row.comments }}</td>

        <%
            labels = [
                { 'label': 'good', 'title': 'Интересно', 'class': 'positive' },
                { 'label': 'maybe', 'title': 'Возможно', 'class': 'active' },
                { 'label': 'never', 'title': 'Не интересно', 'class': 'negative' }
            ]
        %>
        % for label in labels:
            <td class="{{ label['class'] }}">
                %if row.label == label['label']:
                <a class="ui blue ribbon label">{{ label['label'] }}</a>
                %else:
                <a href="/add_label?label={{ label['label'] }}&redirect={{ redirect }}&id={{ row.id }}">{{ label['title'] }}</a>
                %end
            </td>
        %end
    </tr>
    %end
    </tbody>
</table>