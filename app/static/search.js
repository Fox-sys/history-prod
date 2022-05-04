const search = () => {
    let select = document.body.querySelector('select[name="search_type"]');
    let type = select.options[select.options.selectedIndex].value
    let info = document.body.querySelector('input[class="search"]').value.replace(' ', '-');
    let default_url = '/'
    let url = document.body.querySelector('input[class="url"]')
    if (url === undefined) {
        url = default_url
    }
    else {
        url = url.value
    }
    document.location.href = `${url}?type=${type}&info=${info}`
}