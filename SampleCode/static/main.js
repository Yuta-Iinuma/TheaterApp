"use struct";

// function changeHandler(input_value) {
//     const username = $(input_value).serialize();
//     $.ajax('/show', {
//         type: 'post',
//         data: username,
//         dataType: 'json',
//     }).done(function(data) {
//         console.log('Ajax通信 成功');
        
//         const  message = JSON.parse(data.values).massage
//         $('#midashi').html(message);
//     }).fail(function(data) {
//         console.log('ajax通信 失敗');
//     });
// }

function test_click() {
    $('#output').html('<b>JQuery使用成功</b>');
};

// function test_ajax() {
//     data = {'hoge':'fuga'};
//     json = JSON.stringify(data);
//     $.ajax({
//         type:'POST',
//         url:'/test',
//         data: json,
//         contentType: 'application/json',
//         success: function(msg) {
//             console.log(msg);
//         },
//         error: function(msg) {
//             console.log('error');
//         }
//     });
// }
//  $(function () {
//         $(".onSend").on('click', function () { 
//           var obj = document.forms["example_form"];
//           $.ajax("/static/jquery.min.js", {
//             type: 'post',
//             data: $(obj).serialize(), 
//             dataType: 'json'
//           }).done(function(data) {
//             console.log("成功");
//           }).fail(function(data) {
//             console.log("失敗");
//           });
//         });
//     });