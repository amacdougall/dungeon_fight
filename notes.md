# Dungeon Fight architectural notes

Game sequence alternates between world and combat modes. In explore and combat
modes. In explore mode, the user inputs movement commands and, where enemies
are present, can opt to attack them. (Party management is to be completely
ignored for the moment.) In combat mode, the player inputs a command for each
party member, and then party and enemy actions are resolved at once.

The most obvious way to handle the two modes is for each to implement a loop,
with a top-level control context which notices when combat has ended and hands
control back to the explore loop. In fact, the entire combat loop can probably
exist within a single combat(party, enemy) command or something. 

So we can have an ExploreMode which loads a map and places the user into it,
and maintains any other information necessary. CombatMode handles the combat
loop. Game would be the top level, for now, and is mostly responsible for
setting up ExploreMode.

## Command Interpretation

Break input on whitespace and pass the result to an interpreter class. What
happens then depends on how complicated we want to get: we could pass back a
command object which has the ability to execute the action; this would help
with undo, but undo isn't relevant to this kind of game anyway. ...it makes
more sense to send back a command object which has metadata about the command
the user ultimately requested. This gives the interpreter responsibility for
syntax, synonyms, and so on; it just has to map the user input to a concrete
action. This means it has to know about every action in the game, but so what?

# Combat

Let's go with a system where passing an object into a factory generates a
skill action associated with a string. Type the minimum letters which
unambiguously match that string and you're good to go for that character. The
second word of the command should be the target enemy. For instance, given a)
an orc and b) a wolf, and you have the powers "slash", "stab", and "herb", the
command "sl a" slashes the orc; "st b" stabs the wolf; "s a" is ambiguous and
gives an error; and "h" unambiguously uses the herb. 

## Stats

### Attack Power

There's no earthly reason for fighters to cast spells or for mages to fight, so
let's give everyone a generic _Attack Power_ and just not give mages physical
attacks in the first place. I'm dubious about the usefulness of defensive power
in this kind of game; smart enemies should just focus on the mage, right? Not
sure I want to get too much into "smart" enemies, though. That's not really what
this is about. How do we make it reasonable for mages to have low defense, low
health, or both? Traditionally it was to balance out their high attack power.
Let's say that mages have more magical defenses, and they get to choose: attack
sooner, forgoing defenses; or bring up one of a variety of defenses with
increasing power (damage mitigation, damage avoidance, damage reflection) and
increasing drawbacks (up-front mana cost, disables some spells, inflicts slow).

We can make combat last longer, to avoid the imbalance that comes from
traditional spellcaster DPS frontloading.

So everyone has attack power, and there is no defense rating per se. Fighter
types just have more health, and might get damage mitigation as an intrinsic.

### Hit Points

Pretty standard stuff here. Rises as a function of level and class, simple as
that. Like, start it on some base amount and apply a multiplier per level. It
can be as easy as "hp per level: 100".

### Evade and Accuracy Percentages

Not sure how I want to handle this. I want to minimize the chance of someone
whiffing a huge move; or rather, I want the miss chance to be a risk the
attacker takes on. Let's say that evasion is a power you can activate, with its
own rules, and without it, everyone always hits.

### Magic Points

Magic points start full, are drained by spells, and regenerate over time.
Spellcasters have magic points.

### Rage Points

Rage points start empty, build when damage is dealt or received, and are drained
by special attacks. A full rage meter can be used up in a rage explosion, which
grants increases the rage points beyond their normal maximum, but prevents the
user from gaining more rage until the current points are burned. Aggressive
warriors have rage points.

### Super Points

Super points rise under special circumstances, and enable big cool attacks.
Let's implement this later.

## Using Abilities

I guess each class has abilities, which are unlocked based on level; each
ability is an instance of a class, I guess, and it gets applied to the target.
So if I have a level 5 Wizard, and he should have Fireball, we create a new
Fireball(wizard), which generates a fireball instance of the appropriate power
for that character. Then maybe the character has ability lists: action,
reaction, passive. PCs get to choose from action abilities. Ability invocation
can be as simple as `guy.action("fireball", target)`.

Abilities can be added or removed by buffs or debuffs; for instance, a damage
aura might be implemented as a reaction ability.
