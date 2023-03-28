const trArray = document.getElementsByTagName("tr");
const table = {};
// Second i > 34 (last number + 3, example 31 + 3 = 34)
Object.entries(trArray).forEach((t, i) => {
  if (i < 4 || i > 34) return false;
  const td = Object.entries(t[1].children)[1][1];
  let foundValue = "";

  if (td.innerText !== "") {
    foundValue = td.innerText;
  } else {
    Object.entries(td.children).forEach((tdc, tdcI) => {
      const tdAfter = window.getComputedStyle(tdc[1], ":after");
      foundValue += tdAfter.content.replaceAll('"', "");
    });
  }

  table[i - 3] = foundValue;
});

console.log(JSON.stringify(table));
