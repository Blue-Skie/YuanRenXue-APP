Java.perform(function () {
    let ChallengeThreeFragment = Java.use("com.yuanrenxue.match2022.fragment.challenge.ChallengeThreeFragment");
    ChallengeThreeFragment.crypto.implementation = function (str, j) {
        console.log('crypto is called:' + str + '  ' + j);
        let ret = this.crypto(str, j);
        console.log('crypto ret value is ' + ret);
        return ret;
    };

    let f = Java.use("java.lang.Integer");
    f.valueOf.overload('int').implementation = function (a) {
        console.log('getResources is called ' + a);
        let ret = this.valueOf(a);
        console.log('getResources ret value is ' + ret);
        return ret;
    };
});