const fs = require("fs");
const path = require("path");

fs.readFileSync(".env")
    .toString()
    .split(/(\r\n|\n)/g)
    .map((line) => line.split("=", 2))
    .forEach(([k, v]) => {
        if (!process.env[k]) process.env[k] = v;
    });

const parseEnv = (str) =>
    str.replace(/(\$\[([A-z0-9_-]*?)\])/g, (match, ...p) => {
        if (!process.env[p[1]])
            throw new Error(`environment variable ${p[1]} not found`);
        return process.env[p[1]] || "???";
    });

(function build(dir) {
    const odir = parseEnv(path.join("build", dir));

    if (!fs.existsSync(odir))
        fs.mkdirSync(odir, {
            recursive: true,
        });

    for (let p of fs.readdirSync(dir, {
        withFileTypes: true,
    })) {
        const fname = path.join(dir, p.name);

        if (p.isDirectory()) build(fname);
        else if (p.isFile()) {
            fs.writeFileSync(
                parseEnv(path.join(odir, p.name)),
                parseEnv(fs.readFileSync(fname).toString())
            );
        } else {
            console.warn("unsupported", p);
        }
    }
})(process.argv[2]);
