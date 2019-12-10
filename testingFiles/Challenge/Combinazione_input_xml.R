library(xml)
xml <- xmlInternalTreeParse("01.xml")

jobs <- xml["//root/job"]

combinazioni_iniziali <- matrix(nrow = 0, ncol = 3)

routings <- matrix(nrow = 0, ncol = 0)

#Per ogni job
for (i in 1:length(jobs)) {
    j = 4
    #Per ogni multiple_routings_list_elem
    while(length(jobs[[i]][[j]]) != 0) {
        k = 2
        #Per ogni time_profile_list_elem
        while(length(jobs[[i]][[j]][[k]]) != 0) {
            
            #Crea una tripla id_job, id_res_multiple_routing, id_time_profile
            
            combinazioni_iniziali <- rbind(combinazioni_iniziali, c(xmlValue(jobs[[i]][[1]]) ,xmlValue( jobs[[i]][[j]][[1]]), xmlValue(jobs[[i]][[j]][[k]][[1]])))
            
            k = k+1
        }
        
        j = j+1
    }
    
    
    
}



for (i in 1:dim(combinazioni_iniziali)[1]) {
    

}





addChildren(node=jobs[[1]],xmlClone(mrl[[1]]))


doc = xmlInternalTreeParse("01.xml", useInternal = TRUE)
top = xmlRoot(xml)

xpathSApply(top, "//job", xmlValue)
xmlGetAttr(top, "//job")
 lapply(jobs, function(jobs), xmlSApply(top, "//jobs" xmlValue))
lapply(jobs[[1]], function(x) "multiple_routings_list_elem")
