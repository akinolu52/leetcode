function groupAnagrams(strs: string[]): string[][] {
    let strsMapping: Record<string, Array<string>> = {};

    for (const str of strs) {
        const sortedStr = [...str].sort((a, b) => a.localeCompare(b)).join('');
        const prev = strsMapping[sortedStr];

        if (prev) {
            strsMapping[sortedStr] = [...prev, str];
        } else {
            strsMapping[sortedStr] = [str];
        }
    }

    return Object.values(strsMapping);
};
