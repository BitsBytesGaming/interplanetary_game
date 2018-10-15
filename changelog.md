# interplanetary_changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Planned features (backlog)
- Resources and trading
- Reputation
- Faction control

## Current tasks
- Update changelog.md, readme.md
- Write sector keys
- Update sector names, descriptions, and examination strings

## [[0.0.8] - 2018-10-01

### Added
- Simplify starting questions with integer inputs

### Changed
- Correct strings directly involved with starting questions

## [0.0.7] - 2018-09-19

### Added
- Add information to shift to numerical inputs with boxed text

## [0.0.6] - 2018-09-13

### Added
- Write sector names, descriptions and examination strings

### Changed
- Replace single-use player_loot() with multiple-use system
- Switch some player job attributes due to balance concerns

## [0.0.5] - 2018-09-11

### Added
- Create player_money() function (prints the current value of money owned by the player)

### Changed
- Switch all line printouts in functions to per-character functions using sys.stdout and time.sleep() libraries

## [0.0.4] - 2018-09-10

### Added
- Create player_loot() function (loots a sector for a random amount of credits, currently can only be done once per sector)

## [0.0.3] - 2018-09-07

### Added
- Create player_puzzle() function (checks current sector for solved status)
- Add question3 inside setup_game() to obtain job choice
- Add sector solve code segments in zonemap dictionary

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
