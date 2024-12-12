#import "Basic";
#import "String";
#import "File";

main :: () {
    filename := "input.txt";
    //filename := "sample.txt";
    file_contents, ok := read_entire_file(filename);
    if !ok {
        log("File % not found", filename);
        return;
    }

    lines := split(file_contents, "\n");
    for lines {
        log("Line %", it);
    }
}
