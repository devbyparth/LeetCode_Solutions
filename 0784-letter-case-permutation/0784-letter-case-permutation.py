class Solution:
  def letterCasePermutation(self, s: str) -> List[str]:
    res = []

    def backtrack(index: int, seq: list):
      if index == len(s):
        res.append("".join(seq))
        return

      if s[index].isalpha():
        # Choice 1: Lowercase
        seq.append(s[index].lower())
        backtrack(index + 1, seq)
        seq.pop()  # Backtrack

        # Choice 2: Uppercase
        seq.append(s[index].upper())
        backtrack(index + 1, seq)
        seq.pop()  # Backtrack
      else:
        # Single Choice: Digit
        seq.append(s[index])
        backtrack(index + 1, seq)
        seq.pop()  # Backtrack

    backtrack(0, [])
    return res