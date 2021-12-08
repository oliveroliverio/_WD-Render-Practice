import './ExpenseItem.css'

function ExpenseItem(){
  
  return (
    <div>
      <div>{date}</div>
      <div>
        <h2>{item}</h2>
        <div>{price}</div>
      </div>
    </div>
  )
}

export default ExpenseItem;