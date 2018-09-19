# interplanetary_changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2018-09-02

### Added
- Create start menu
- Create initial player questions
- Create myPlayer class (for storage of player information)
- Create dictionary zonemap (for storage of map sector information)
- Add prompt() function (prompts player for a valid command until the game is complete)

## [0.0.2] - 2018-09-05

### Added
- Create player_move() function (moves player in the requested cardinal direction or relative direction)
- Create movement_handler() function (lists sector the player moved to with player_move() and brief information about it)
- Create player_examine() function (prints information about the currently occupied sector)
- Add player inventory (not implemented)

### Changed
- Correct directional inputs in zonemap dictionary
- Add print_location() function (procedural boxed text w/calibration)

