
# my input
#Player 1 starting position: 8
#Player 2 starting position: 6


"""
--- Part Two ---
Now that you're warmed up, it's time to play the real game.
A second compartment opens, this time labeled Dirac dice. Out of it falls a single three-sided die.
As you experiment with the die, you feel a little strange. An informational brochure in the compartment explains that this is a quantum die: when you roll it, the universe splits into multiple copies, one copy for each possible outcome of the die. In this case, rolling the die always splits the universe into three copies: one where the outcome of the roll was 1, one where it was 2, and one where it was 3.
The game is played the same as before, although to prevent things from getting too far out of hand, the game now ends when either player's score reaches at least 21.
Using the same starting positions as in the example above, player 1 wins in 444356092776315 universes, while player 2 merely wins in 341960390180808 universes.
Using your given starting positions, determine every possible outcome. Find the player that wins in more universes; in how many universes does that player win?
"""


p1loc = 8
p2loc = 6


p1score = 0
p2score = 0

die = 0
rolls = 0

def roll():
    global die
    global rolls
    rolls += 1
   
    die = die + 1
    if die > 100:
        die = 1
    return die


while True:
    p1loc = p1loc + roll()
    p1loc = p1loc + roll()
    p1loc = p1loc + roll()
    p1loc = p1loc % 10
    if p1loc == 0:
        p1loc = 10
    p1score += p1loc
    if p1score >= 1000:
        print(f"P1: {p1loc} {p1score}")
        print(f"P2: {p2loc} {p2score}")
        print(rolls)
        break
       

    p2loc = p2loc + roll()
    p2loc = p2loc + roll()
    p2loc = p2loc + roll()
    p2loc = p2loc % 10
    if p2loc == 0:
        p2loc = 10

    p2score += p2loc
    if p2score >= 1000:
        print(f"P1: {p1loc} {p1score}")
        print(f"P2: {p2loc} {p2score}")
        print(rolls)
        break

if p1score < p2score:
    print(rolls*p1score)
else:
    print(rolls*p2score)
        
