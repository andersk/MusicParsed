/**
 * @file Everything related to single notes.
 */

import "core-js/fn/array/flat-map";

const accidentalFifths: [string, number][] = [
  ["bb", -14],
  ["𝄫", -14],
  ["b", -7],
  ["♭", -7],
  ["", 0],
  ["#", 7],
  ["♯", 7],
  ["x", 14],
  ["𝄪", 14],
];
const letterFifths: [string, number][] = [
  ["F", -1],
  ["C", 0],
  ["G", 1],
  ["D", 2],
  ["A", 3],
  ["E", 4],
  ["B", 5],
];
const pitchFifths: [string, number][] = accidentalFifths.flatMap(af =>
  letterFifths.map((lf): [string, number] => [lf[0] + af[0], lf[1] + af[1]])
);

export const pitchToFifths: Map<string, number> = new Map(pitchFifths);
export const fifthsToPitch: Map<number, string> = new Map(
  pitchFifths.map((pf): [number, string] => [pf[1], pf[0]])
);

export const noteRegex = /[A-G](?:bb|𝄫|b|♭|#|♯|x|𝄪)?/g;
