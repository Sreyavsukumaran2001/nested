weather=[{"district":"pkd","temp":30},
        {"district":"mlp","temp":29},
        {"district":"thrs","temp":24},
        {"district":"kannur","temp":28},
        {"district":"thrs","temp":29}
          ]

out={}
for data in weather:
    dist_name=data["district"]
    cur_temp=data["temp"]
    if dist_name in out:
        old_temp=out[dist_name]
        if cur_temp >old_temp:
            out[dist_name]=cur_temp
    else:
        out[dist_name]=cur_temp
print(out)

srt_out=sorted(out.items(),key=lambda item:item[1],reverse=True )
print(srt_out)