describe("Type of Examples when passed different parameters", function() {
    it("It should return a string when passed a string", function() {
        expect(testTypeOf("Hello world!")).toEqual("string");
    });

    it("It should return a number when passed a number", function() {
        expect(testTypeOf(9)).toEqual("number");
    });

    it("It should return a object when passed null", function() {
        expect(testTypeOf(null)).toEqual("object");
    });

});