function vowels(s: string): number {
    s = s.toLowerCase().replace(/[^aeiou]/g, '');

    return s.length
};

let s;
s = "A man, a pelan,9 a canalp: Panama";

console.log(vowels(s))