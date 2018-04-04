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
/*
function callback(data) {
    var oNews = document.getElementsByClassName('news_')[0];
    var newsht='';
    for(var item in data.results){
        newsht += htadd(data.results[item]);
    }
    oNews.innerHTML=newsht;
}*/
