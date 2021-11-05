function togglePopup() {
    document.getElementById("popup-1").classList.toggle("active");
}
function togglePopupdua() {
    document.getElementById("popup-2").classList.toggle("active");
}
function togglePopuptiga() {
    document.getElementById("popup-3").classList.toggle("active");
}

fetch("https://v1.nocodeapi.com/rafiatha11/xml_to_json/XAEksBgurJJkpFsB?url=https://covid19.go.id/feed/masyarakat-umum")
    .then(response => response.json())
    .then(response => {
        const items = response?.rss?.channel?.item
        const item_satu = items[0]
        const item_dua = items[1]
        const item_tiga = items[2]

        document.getElementById("judul_satu").innerHTML = item_satu.title
        document.getElementById("judul_dua").innerHTML = item_dua.title
        document.getElementById("judul_tiga").innerHTML = item_tiga.title

        document.getElementById("judul_satu_pop").innerHTML = item_satu.title
        document.getElementById("judul_dua_pop").innerHTML = item_dua.title
        document.getElementById("judul_tiga_pop").innerHTML = item_tiga.title

        document.getElementById("desc_satu").innerHTML = item_satu.description.slice(0, 75) + "....."
        document.getElementById("desc_dua").innerHTML = item_dua.description.slice(0, 75) + "....."
        document.getElementById("desc_tiga").innerHTML = item_tiga.description.slice(0, 75) + "....."

        document.getElementById("desc_satu_pop").innerHTML = item_satu.description
        document.getElementById("desc_dua_pop").innerHTML = item_dua.description
        document.getElementById("desc_tiga_pop").innerHTML = item_tiga.description

    });
