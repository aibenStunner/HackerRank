'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    [...s].forEach(c => 'aieou'.includes(c) ? console.log(c) : null);
    [...s].forEach(c => 'aieou'.includes(c) ? null : console.log(c));
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
main()
