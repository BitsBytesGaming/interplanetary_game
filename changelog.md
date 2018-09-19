# interplanetary_changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.5] - 2018-09-11

### Added
- Create player_money() function (prints the current value of money owned by the player)

## [0.0.4] - 2018-09-10

### Added
- Create player_loot() function (loots a sector for a random amount of credits, currently can only be done once per sector)

## [0.0.3] - 2018-09-07

### Added
- Create player_puzzle() function (checks current sector for solved status)
- Add question3 inside setup_game() to obtain job choice

### Changed
- Switch main player jobs to dynamically configure player point values in myPlayer class rather than random values

## [0.0.2] - 2018-09-05

### Added
- Create player_move() function (moves player in the requested cardinal direction or relative direction)
- Create movement_handler() function (lists sector the player moved to with player_move() and brief information about it)
- Create player_examine() function (prints information about the currently occupied sector)
- Add player inventory (not implemented)

### Changed
- Correct directional inputs in zonemap dictionary
- Add print_location() function (procedural boxed text w/calibration)

## [0.0.1] - 2018-09-02

### Added
- Create start menu
- Create setup_game() function (initial player questions)
- Create myPlayer class (for storage of player information)
- Create dictionary zonemap (for storage of map sector information)
- Add prompt() function (prompts player for a valid command until the game is complete)
- Add main_game_loop() function (runs prompt() until game is over)
