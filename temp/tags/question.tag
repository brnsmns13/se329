<question>
    <button onclick={ del_btn } class="btn btn-xs btn-danger pull-right">Delete</button>
    <button onclick={ edit_btn } class="btn btn-xs btn-primary pull-right">Edit</button>
    { opts.data.question }

    <script>

        del_btn(event) {
            console.log(event);
        }

        edit_btn(event) {
            opts.edit_callback(opts.data);
        }

    </script>
</question>
