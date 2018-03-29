$(function () {
    navIndex(0);
    $.ajax({
        url: '/api/newsinfo/',
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
    var oNews = document.getElementsByClassName('news_')[0];
    var newsht='';
    for(var i=0; i<data.results.length; i++){
        newsht += htadd(data.results[i]);
    }
    oNews.innerHTML=newsht;
    imgSize();
}

function htadd(data,cla) {
    var ht='';
    ht+=' <div class="first">';
	ht+='<div class="news_content"><div class="img_left">';
	ht+='<img src="' + data.news_image1 + '"/></div><div class=\"con_right\">';
	ht+='<a class="con" href="newsDetails.html">' + data.news_content + '</a></div></div></div>';
	return ht;
}
function imgSize() {
    var oNews = document.getElementsByClassName('news_')[0];
    imgs = oNews.getElementsByTagName('img');
    for(var i=0; i<imgs.length; i++){
        if (imgs[i].clientHeight>imgs[i].clientWidth){
            imgs[i].style.height='100%';
        }else {
            imgs[i].style.width='100%';
        }
    }
}