<question-box>
    <div class="row">
        <div class="col-md-6">
            <question-form question_data={ q_form } handle={ handle_question }></question-form>
        </div>
        <div class="col-md-6">
            <question-list edit_callback={ edit_event } data={ questions }></question-list>
        </div>
    </div>

    <script>
        handle_question(q_data) {
            this.questions.push(q_data);
            this.update({data: this.questions});
        }

        edit_event(q_data) {
            this.update({q_form: q_data})
        }

        this.questions = [];
    </script>
</question-box>
