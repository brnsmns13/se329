<question-list>
    <h1>Questions</h1>
    <ul class="list-group">
        <li each={ opts.data } class="list-group-item">
            <question edit_callback={ opts.edit_callback } data={ this }></question>
        </li> 
    </ul>
</question-list>
