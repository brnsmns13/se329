riot.tag('question-box', '<div class="row"> <div class="col-md-6"> <question-form question_data="{ q_form }" handle="{ handle_question }"></question-form> </div> <div class="col-md-6"> <question-list edit_callback="{ edit_event }" data="{ questions }"></question-list> </div> </div>', function(opts) {
        this.handle_question = function(q_data) {
            this.questions.push(q_data);
            this.update({data: this.questions});
        }.bind(this);

        this.edit_event = function(q_data) {
            this.update({q_form: q_data})
        }.bind(this);

        this.questions = [];
    
});

riot.tag('question-form', '<h1>Enter Question</h1> <form> <input name="question" type="text" class="form-control" placeholder="Enter Question"> <hr> <div class="form-group"> <input name="a1" type="text" class="form-control" placeholder="Answer 1"> </div> <div class="form-group"> <input name="a2" type="text" class="form-control" placeholder="Answer 2"> </div> <div class="form-group"> <input name="a3" type="text" class="form-control" placeholder="Answer 3"> </div> <div class="form-group"> <input name="a4" type="text" class="form-control" placeholder="Answer 4"> </div> <div class="form-group"> <button onclick="{ save_question }" class="btn btn-success">Save Question</button> <button onclick="{ submit_quiz }" class="btn btn-primary">Submit Quiz</button> </div> </form>', function(opts) {
        
        this.save_question = function(event) {
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
        }.bind(this);

    
});

riot.tag('question-list', '<h1>Questions</h1> <ul class="list-group"> <li each="{ opts.data }" class="list-group-item"> <question edit_callback="{ opts.edit_callback }" data="{ this }"></question> </li> </ul>', function(opts) {

});

riot.tag('question', '<button onclick="{ del_btn }" class="btn btn-xs btn-danger pull-right">Delete</button> <button onclick="{ edit_btn }" class="btn btn-xs btn-primary pull-right">Edit</button> { opts.data.question }', function(opts) {

        this.del_btn = function(event) {
            console.log(event);
        }.bind(this);

        this.edit_btn = function(event) {
            opts.edit_callback(opts.data);
        }.bind(this);

    
});
