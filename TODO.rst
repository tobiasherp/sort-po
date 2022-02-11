Things to do
============

- configuration file
- sort comments by type
- sort location comments per message id
- options ...
 
  - to strip line numbers (and resulting unique source specs)
  - to have message strings start with an empty string
    in the 1st line (for nicer diffs between language versions)
  - to line-break message ids and strings ...
   
    - after "\n", if present
    - at word borders,
    - after sentences (". "),
    - with a given text-width, or
    - preserve the original format alltogether

  - for `--pipe` mode

- sort message ids ...

  - alphabetically
  - by ASCII order,

    and probably take into account

  - source specs, including line numbers
  - message id relations
