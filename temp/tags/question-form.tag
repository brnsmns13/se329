<question-form>
    <h1>Enter Question</h1>
    <form>
        <input name="question" type="text" class="form-control" placeholder="Enter Question">
        <hr>
        <div class="form-group">
            <input name="a1" type="text" class="form-control" placeholder="Answer 1">
        </div>
        <div class="form-group">
            <input name="a2" type="text" class="form-control" placeholder="Answer 2">
        </div>
        <div class="form-group">
            <input name="a3" type="text" class="form-control" placeholder="Answer 3">
        </div>
        <div class="form-group">
            <input name="a4" type="text" class="form-control" placeholder="Answer 4">
        </div>
        <div class="form-group">
            <button onclick={ save_question } class="btn btn-success">Save Question</button>
            <button onclick={ submit_quiz } class="btn btn-primary">Submit Quiz</button>
        </div>
    </form>

    <script>
        
        save_question(event) {
            opts.handle({
                question: this.question.value.trim(),
                a1: this.a1.value.trim(),
                a2: this.a2.value.trim(),
                a3: this.a3.value.trim(),
                a4: this.a4.value.trim(),
            });

            this.question.value = '';
            this.a1.value = '';
            this.a2.value = '';
            this.a3.value = '';
            this.a4.value = '';
        }

    </script>
</question-form>
