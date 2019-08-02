function getCurrentMemeId() {
    let img = document.querySelector("body > img");
    src_link = img.src;
    return src_link.split("/meme/")[1]
}

function genData(dank_flag) {
    return JSON.stringify({
        'meme_id': getCurrentMemeId(),
        'dank_flag': dank_flag
    })
}

function sendData(data) {
    fetch("/rank",
    {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: "POST",
        body: data
    })
    .then(resp => {
         console.log(resp)
         location.reload();
    });
}

function onRankClick(dank_flag) {
    data = genData(dank_flag);
    sendData(data)

}