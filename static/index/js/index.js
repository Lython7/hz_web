$(function () {
    var url_ = 'api/news/';

    $.ajax({
        url: url_,
        type: "GET",
        success: function(data){
            console.log(data);
        }
    });
});