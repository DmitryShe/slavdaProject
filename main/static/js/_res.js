

export function getFetch() {
    let address = document.location.href;

    fetch(address)
    .then((res) => {
        return res.json();
    })
    .then((data) => {
        console.log(data);
    });
}