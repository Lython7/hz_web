$(function () {
    var url_ = '../data/news.json';
    $.ajax({
        url: url_,
        type: "GET",
        success: function(data){
            console.log(data);
        }
    });
});