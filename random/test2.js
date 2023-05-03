
let grid = ["      ######",
    "###   #    ####",
    "# #####       #",
    "#           ###",
    "###         #  ",
    "  #         #  ",
    "###         ###",
    "#       ##    #",
    "###   ##  # ###",
    "  #   #  ###",
    "  #####",]

const detectExteriorCells = grid => {
    // console.log(grid);
    let result = [];

    for (let i = 0; i < grid.length; i++) {
        const row = grid[i];
        let noSpace = true
        let _result = [];

        for (let j = 0; j < row.length; j++) {
            const column = grid[i][j];
            console.log('column => ', column);

            if (column == ' ') {
                if (noSpace) {
                    // _result += '.';
                    _result.push('.')
                } else {
                    // _result += ' ';
                    _result.push(' ')
                }
            } else {
                noSpace = false;
                // result += column
                _result.push(column)

            }

        }

        // console.log('_result => ', _result);
        const newResult = _result.join('');
        result = [...result, newResult];
        // result.push(_result);
        console.log('\n');
    }

    return result;
};


console.log(detectExteriorCells(grid))