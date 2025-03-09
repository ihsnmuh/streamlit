import streamlit as st
from lib.task import Task
from lib.task_manager import TasksManager

# Inisialisasi session state untuk menyimpan task
if "task_manager" not in st.session_state:
    st.session_state.task_manager = TasksManager("My Tasks")

st.title("📋 List Task Kamu")

# Input untuk menambahkan task baru
new_title = st.text_input("Judul Task:")
new_description = st.text_area("Deskripsi Task:")

# Action untuk menambahkan task baru
if st.button("Tambah"):
    if new_title and new_description:
        new_task = Task(new_title, new_description)
        st.session_state.task_manager.add_task(new_task)
        st.success("Task berhasil ditambahkan!")
        st.rerun()
    else:
        st.warning("Judul dan Deskripsi tidak boleh kosong!")

st.write("---")
st.subheader("Daftar task Anda:")

# Menampilkan semua task
tasks = st.session_state.task_manager.get_all_tasks()

status_option = ["todo", "in-progress", "done"]

if not tasks :
    st.info("Belum ada task.")
else:
    
    col1, col2, col3 = st.columns([1,1,1])
        
    with col1:
        st.error("💡 Todo")
        for idx, task in enumerate(tasks):
            if task.status == "todo":
                with st.expander(f"📋 {str(task.title).capitalize()}"):
                    st.write(task.description)

                    new_status = st.selectbox(
                        "Status:", status_option, 
                        index=["todo", "in-progress", "done"].index(task.status),
                        key=f"status_{idx}"
                    )
                    
                    if new_status != task.status:
                        task.change_status(new_status)
                        st.rerun()
                        
                    delete_btn = st.button("", key=f"delete_{idx}",icon="🗑️")
                    if delete_btn:
                        st.session_state.task_manager.delete_task(idx)
                        st.rerun()
                        
        with col2:
            st.warning("🔄 In-Progress")
            for idx, task in enumerate(tasks):
                if task.status == "in-progress":
                    with st.expander(f"📋 {str(task.title).capitalize()}"):
                        st.write(task.description)

                        new_status = st.selectbox(
                            "Status:", status_option, 
                            index=["todo", "in-progress", "done"].index(task.status),
                            key=f"status_{idx}"
                        )
                    
                        if new_status != task.status:
                            task.change_status(new_status)
                            st.rerun()
                            
                        delete_btn = st.button("", key=f"delete_{idx}",icon="🗑️")
                        if delete_btn:
                            st.session_state.task_manager.delete_task(idx)
                            st.rerun()
                                
        with col3:
            st.success("🎉 Done")
            for idx, task in enumerate(tasks):
                if task.status == "done":
                    with st.expander(f"📋 {str(task.title).capitalize()}"):
                        st.write(task.description)

                        new_status = st.selectbox(
                            "Status:", status_option, 
                            index=["todo", "in-progress", "done"].index(task.status),
                            key=f"status_{idx}"
                        )
                        
                        if new_status != task.status:
                            task.change_status(new_status)
                            st.rerun()
                            
                        delete_btn = st.button("", key=f"delete_{idx}", icon="🗑️")
                        if delete_btn:
                            st.session_state.task_manager.delete_task(idx)
                            st.rerun()