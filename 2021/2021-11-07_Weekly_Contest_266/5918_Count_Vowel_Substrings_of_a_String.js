function checkVowels(w) {
    return w.indexOf("a") > -1 &&
    w.indexOf("e") > -1 &&
    w.indexOf("i") > -1 &&
    w.indexOf("o") > -1 &&
    w.indexOf("u") > -1;
}

function getAllSubstrings(str, minLength) {
    let result = [];
  
    for (let i = 0; i < str.length; i++) {
        for (let j = i + minLength; j < str.length + 1; j++) {
            result.push(str.slice(i, j));
        }
    }
    return result;
}

/**
 * @param {string} word
 * @return {number}
 */
var countVowelSubstrings = function(word) {
    substrings = [];
    let vowels = 'aeiou'
    let current_sub = ""
    for (let i = 0; i < word.length; i++) {
        if (vowels.indexOf(word[i]) > -1) {
            current_sub += word[i];
        } else {
            substrings.push(current_sub);
            current_sub = "";
        }
        if (i === word.length - 1) {
            substrings.push(current_sub);
        }
    }
    console.log(substrings);

    let countRes = 0;
    for (let i = 0; i < substrings.length; i++) {
        if (substrings[i].length >= 5) {
            let allSubStr = getAllSubstrings(substrings[i], 5);
            console.log(allSubStr);
            for (let j = 0; j < allSubStr.length; j++) {
                if (checkVowels(allSubStr[j])) {
                    countRes++;
                }
            }
        }
    }
    return countRes;
};
