$(function () {
    navIndex(1);
    $.ajax({
        url: '../api/news/' + localStorage.getItem('newsId'),
        type: 'GET',
        success: function(data) {
            console.log(data);
            callback(data);
        },
        error: function(xhr, textStatus) {
            alert('加载失败，请稍后再试！');
            console.log(xhr);
            console.log(textStatus);
        }
    });
});
function callback(data) {
    var oNews = document.getElementsByClassName('details')[0];
    var time = data.news_time.split('T')[0];
    var newsht = '';
    newsht += '<h1 class="title">' + data.news_title + '</h1>';
    newsht += '<div class="time">' + time + '</div>';
    for (var i=1; i<=20; i++) {
        if (data['news_image'+i]){
            newsht+='<div class="img"><img src="' + data['news_image'+i] + '"/></div>';
        }
        if (data['news_content'+i]){
            newsht+='<p>' + data['news_content'+i] + '</p>';
            console.log(1)
        }
    }
    oNews.innerHTML=newsht;
}
