!mkdir clusterSMC

~/prism-games-csg-dev/prism/bin/prism 26Point2_1_1.prism 26Point2_manual.props -javamaxmem 700g -const no_spaces=50 -prop 1 > clusterSMC/random_winrate_50.log

~/prism-games-csg-dev/prism/bin/prism 26Point2_4_2.prism 26Point2_manual.props -javamaxmem 700g -const no_spaces=50 -prop 1 > clusterSMC/winrate_4_against_2.log

~/prism-games-csg-dev/prism/bin/prism 26Point2_5_3.prism 26Point2_manual.props -javamaxmem 700g -const no_spaces=50 -prop 1 > clusterSMC/hybrid_against_3.log

~/prism-games-csg-dev/prism/bin/prism 26Point2_3_4.prism 26Point2_manual.props -javamaxmem 700g -const no_spaces=50 -prop 1 > clusterSMC/3_against_4.log

~/prism-games-csg-dev/prism/bin/prism 26Point2_5_4.prism 26Point2_manual.props -javamaxmem 700g -const no_spaces=50 -prop 1 > clusterSMC/hybrid_against_4.log

~/prism-games-csg-dev/prism/bin/prism 26Point2_0_3.prism 26Point2_manual.props -javamaxmem 700g -const no_spaces=50 -prop 1 > clusterSMC/nondet_against_3.log

~/prism-games-csg-dev/prism/bin/prism 26Point2_0_3.prism 26Point2_manual.props -javamaxmem 700g -const no_spaces=30 -prop 1 > clusterSMC/nondet_against_3_small.log

