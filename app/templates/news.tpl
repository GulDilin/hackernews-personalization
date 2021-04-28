%rebase('base.tpl', title='News', path='news')
% include('news_table.tpl')
<table>
    <tr>
        <td colspan="7">
            <a href="/update_news?next_id={{ next_id }}" class="ui right floated small primary button">I Wanna more
                Hacker News!</a>
        </td>
    </tr>
</table>
