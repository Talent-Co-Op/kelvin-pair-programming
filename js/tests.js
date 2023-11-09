const maximizeLuckBalance = require('./solution');

class TestMaximizeLuckBalance {

    testCase1() {
        let contests = [[5, 1], [2, 1], [1, 1], [8, 0], [10, 0], [5, 0]];
        let k = 3;
        console.assert(maximizeLuckBalance(contests, k) === 29);
    }

    testCase2() {
        let contests = [[1, 0]];
        let k = 0;
        console.assert(maximizeLuckBalance(contests, k) === 1);
    }

    testCase3() {
        let contests = [[3, 0], [7, 0], [2, 0], [9, 0]];
        let k = 2;
        console.assert(maximizeLuckBalance(contests, k) === 21);
    }

    // Add more test cases as needed

}

const tests = new TestMaximizeLuckBalance();
tests.testCase1();
tests.testCase2();
tests.testCase3();
// Add more test cases as needed
