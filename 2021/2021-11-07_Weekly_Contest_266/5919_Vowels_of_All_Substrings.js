function checkIfVowel(c) {
    if (c === "a" || c === "e" || c === "i" || c === "o" ||c === "u") {return 1;}
    return 0;
}

const arrSum = array => array.reduce((sum, num) => sum + (Array.isArray(num) ? arrSum(num) : num * 1), 0);

/**
 * @param {string} word
 * @return {number}
 */
 var countVowels = function(word) {
    let matrix = new Array(word.length).fill(new Array(word.length).fill(0));
    console.table(matrix);
    
    for (let i = 1; i < word.length; i++) {
        for (let j = i + 1; j < word.length; j++) {
            console.log("i =", i, ". j =", j);
            console.log("char at j:", word.charAt(j));
            matrix[i][j] += matrix[i][j - 1] + checkIfVowel(word.charAt(j - 1));
            console.table(matrix);
        }
    }
    return arrSum(matrix);
};
