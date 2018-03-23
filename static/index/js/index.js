$(function () {
    navIndex(0);
    $.ajax({
        url: '/api/news/',
        type: 'GET',
        success: function(data) {
            console.log(data);
            pipeDataShow(data, callback);
        },
        error: function(xhr, textStatus) {
            alert('加载失败，请稍后再试！');
            console.log(xhr);
            console.log(textStatus);
        }
    });
});
