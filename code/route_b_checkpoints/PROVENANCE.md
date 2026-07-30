# Provenance — route B pipeline checkpoints

- generator code: admissibility/o25/code/spectral_O12.py @ commit c86561e1871a7f18a549227f53f0bebbb6cf2652 (o25 repo)
- data repo commit: 2e904cc95ce51ad58e53b4568bb800aafa71a349 (o14 repo)
- BFS: depth-capped variant of o12.bfs_shells (identical layers; stopping rule only)
- frozen n_cut = stored n1: {29: 5, 61: 7, 101: 10, 151: 12, 211: 13}
- reproduction: PYTHONPATH=<numpy+matplotlib> python3 route_b_pipeline_tests.py

- q29_o12.npz sha256 = 3401b5832300d17ed6fa7cbf45f6b1de374974795c888b15db850a116b204d6e; seed=0; n1=5; blocks[0]=[27, 8, 14]
- q61_o12.npz sha256 = 710347c7b4edeab49dc34bbc0e304dfe25bbc9e0b3568686eb283ebf9d846946; seed=0; n1=7; blocks[0]=[34, 19, 5]
- q101_o12.npz sha256 = 6a40212cec6e9036060ffa8bd3aba8bd91a420a743b994a32744360f4a63631a; seed=0; n1=10; blocks[0]=[93, 42, 68]
- q151_o12.npz sha256 = bdc5e3eec4c0b4431bfd446488947c9e0ccdcd072c17352fc904032ab6dbf3b6; seed=0; n1=12; blocks[0]=[95, 76, 126]
- q211_o12.npz sha256 = 5b01138713d60087133413625dd5e24f8a56a0b7f6902aef76f3304a0e4bf332; seed=0; n1=13; blocks[0]=[124, 54, 90]

## OLS log-log slopes (value, residual std)
- slope[aY+] (q>=61) = +0.072 (res std 0.095)
- slope[aY-] (q>=61) = +0.072 (res std 0.095)
- slope[aXc+] (q>=61) = +0.000 (res std 0.000)
- slope[aXc-] (q>=61) = +0.000 (res std 0.000)
- slope[eps_n=0] = +19.913 (res std 10.050)
- slope[eps_n=1] = +19.822 (res std 10.010)
- slope[eps_n=2] = +19.799 (res std 9.948)
- slope[eps_n=3] = +19.900 (res std 9.996)
- slope[eps_n=4] = +19.972 (res std 9.968)
- slope[eps_n=5] = +19.871 (res std 10.047)
- slope[eps_n=6] = +19.917 (res std 9.997)
