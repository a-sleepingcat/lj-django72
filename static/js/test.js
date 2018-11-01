// $(function () {
//     $('img').each(function () {
//         var ss = $(this).attr('src')
//         var imgpath = alert(ss.slice(3))
//         imgpath = "{% static '" +imgpath+ "'%}"
//         $(this).attr('src',imgpath)
//     })
//     console.log($('body').html())
// })


$(function () {
    $('img').each(function () {
        var imgpath = $(this).attr('src')
        while(imgpath[0]="."){imgpath=imgpath.substr(1,)}    imgpath = "{% static '" + imgpath +  "' %}"
        $(this).attr('src', imgpath)
    })

    console.log($('body').html())
})

