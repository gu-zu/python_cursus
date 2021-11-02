//Reads all files and puts them into a single txt file
const fs = require("fs");

const mode = 0; //0 = start file, 1 = append excercises
const from = 1,
    end = 17; //which numbers to add/write

const ws = fs.createWriteStream("opdrachten/all.txt", {
    flags: mode ? "a" : "w",
});
if (mode == 0) ws.write("Python cursus Guus Zuijdgeest - V6 - 2021-2022\r\n");

/*const files = fs.readdirSync("opdrachten", "utf8"); //c could be used to use all files in dir
files.forEach((val) => {
    const no = val.match(/opdr(\d+).py/);
    console.log(val, no ? `nr ${no[1]}` : "not python");
});*/

let i = from - 1;
next();

function next() {
    i++;
    if (i <= end) return writenext(i);
    ws.end();
}

function writenext(i) {
    ws.write("\r\n\r\nOpdracht " + i + ":\r\n", () => {
        const fl = fs.readFileSync("opdrachten/opdr" + i + ".py", "utf8");
        let fl2 = "";
        fl.split("\n").forEach((val) => {
            fl2 += "    " + val + "\r\n";
        });
        ws.write(fl2.substr(0, fl2.length - 2), next);
    });
}
