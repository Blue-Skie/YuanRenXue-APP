Java.perform(function () {
    let ChallengeTwoFragment = Java.use("com.yuanrenxue.match2022.fragment.challenge.ChallengeTwoFragment");
    ChallengeTwoFragment.sign.implementation = function (str) {
        console.log('sign is called: ' + str);
        let ret = this.sign(str);
        console.log('sign ret value is ' + ret);
        return ret;
    };


});