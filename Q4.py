from collections import defaultdict
import itertools as it

source = [75,45,30,35,30,15,60,90,20,10]
targets = [120]

p = [[a for n in range(1, len(source)) for a in it.combinations(source, n) if sum(a) == t] for t in targets]
[dict(zip(targets, a)) for a in it.product(*p) if len(sum(a, tuple())) == len(set(sum(a, tuple())))]

print(p)

from collections import defaultdict
import itertools as it

source = [75,45,30,35,30,15,60,90,20,10]
targets = [120]

p = [[a for n in range(1, len(source)) for a in it.combinations(source, n) if sum(a) == t] for t in targets]
[dict(zip(targets, a)) for a in it.product(*p) if len(sum(a, tuple())) == len(set(sum(a, tuple())))]

print(p)


Pac-man			75	$250
Speed Racer		45	$280
Pump it Up		30	$150
Space Invaders		35	$120
Mario Bros		30	$200
Mortal Kombat		15	$100
Atari Breakout		60	$300
Super Tetris		90	$350
Star Wars		20	$110
Street Fighter II	10	$90



[[(75, 45), 		250+280			530
(30, 90),  		200+350			550
(30, 90), 		
(75, 30, 15), 		250+200+100		550
(75, 35, 10), 		250+120+90		460
(75, 30, 15), 		250+150+100		500		
(45, 15, 60), 		280+100+300		680
(30, 30, 60), 		150+200+300		650
(90, 20, 10),  		350+110+90		550
(75, 15, 20, 10), 	250+100+110+90		550
(45, 30, 35, 10), 	280+150+120+90		640
(45, 30, 30, 15), 	280+200+150+100		730
(45, 35, 30, 10), 	280+120+200+90		690
(30, 60, 20, 10), 	150+300+110+90		650
(35, 15, 60, 10), 	120+300+110+90		620
(30, 60, 20, 10), 	200+300+110+90		700
(45, 30, 15, 20, 10), `280+ 200+100+110+90	780
(45, 30, 15, 20, 10),  280+150+100+110+90	680
(30, 35, 30, 15, 10)]] 200+120+150+100+90	670