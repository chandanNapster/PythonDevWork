Match (a:USER{user_name:"furixturi"}), (b:USER{user_name:"jagyasa-grover"})
With a as a, b as b
Create (a)<-[:FOLLOWS]-(u1:USER{user_name:"Kaijun"}),
        (a)<-[:FOLLOWS]-(u2:USER{user_name:"cusspvz"}),
		(a)<-[:FOLLOWS]-(u3:USER{user_name:"gabrielpconceicao"}),
		(a)<-[:FOLLOWS]-(u4:USER{user_name:"angusshire"}),
		(a)<-[:FOLLOWS]-(u5:USER{user_name:"auycro"}),
		(a)<-[:FOLLOWS]-(u6:USER{user_name:"KlotzAndrew"}),
		(a)<-[:FOLLOWS]-(u7:USER{user_name:"tejanhu"}),
		(a)<-[:FOLLOWS]-(u8:USER{user_name:"sugaf"}),
		(a)<-[:FOLLOWS]-(u9:USER{user_name:"bokinga"}),
		(a)<-[:FOLLOWS]-(u10:USER{user_name:"hakuna16"}),
		(a)<-[:FOLLOWS]-(u11:USER{user_name:"RenatoSad"}),
		(a)<-[:FOLLOWS]-(u12:USER{user_name:"frk008"}),
		(a)<-[:FOLLOWS]-(u13:USER{user_name:"Alexdenova"}),
		(a)<-[:FOLLOWS]-(u14:USER{user_name:"ueiryu"}),
		(b)<-[:FOLLOWS]-(u15:USER{user_name:"rohithadassanayake"}),
		(b)<-[:FOLLOWS]-(u16:USER{user_name:"moueza"}),
		(b)<-[:FOLLOWS]-(u17:USER{user_name:"jikkujose"}),
		(b)<-[:FOLLOWS]-(u18:USER{user_name:"mwalbers1"}),
		(b)<-[:FOLLOWS]-(u19:USER{user_name:"SergeStinckwich"}),
		(b)<-[:FOLLOWS]-(u20:USER{user_name:"JurajKubelka"}),
		(b)<-[:FOLLOWS]-(u21:USER{user_name:"sirinath"}),
		(b)<-[:FOLLOWS]-(u22:USER{user_name:"ajsb85"}),
		(b)<-[:FOLLOWS]-(u23:USER{user_name:"rhnvrm"})
		
		
Match (b:USER)
Where and a.user_name = "jagyasa-grover"		
		