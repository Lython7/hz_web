$(function () {
    $.ajax({
        url: baseUrl + '/investment/check/',
        type: 'GET',
        data: {
            power: sessionStorage.power
        },
        headers: {'Authorization': sessionStorage.token},
        success: function(data) {
            console.log(data);
            pipeDataShow(data, callback);
            /*if(data.length !== 0) {
                callback(data);
            } else {
                document.body.innerHTML = '<p style="font: 36px bold;text-align: center;">暂无待审核数据</p>';
            }*/
        },
        error: function(xhr, textStatus) {
            alert('加载失败，请稍后再试！');
            console.log(xhr);
            console.log(textStatus);
        }
    });
});
